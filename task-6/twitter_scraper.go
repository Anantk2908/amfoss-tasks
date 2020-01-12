package main

import (
	"flag"
	"strconv"
	"fmt"
	"log"
	"os"
	"bufio"

	"github.com/coreos/pkg/flagutil"
	"github.com/dghubble/go-twitter/twitter"
	"golang.org/x/oauth2"
	"golang.org/x/oauth2/clientcredentials"
)

func main() {
	flags := struct {
		consumerKey    string
		consumerSecret string
	}{}
	
	flag.StringVar(&flags.consumerKey, "consumer-key","Your twitter consumer key", "Twitter Consumer Key")
	flag.StringVar(&flags.consumerSecret, "consumer-secret","Your twitter consumer secret", "Twitter Consumer Secret")
	flag.Parse()
	flagutil.SetFlagsFromEnv(flag.CommandLine, "TWITTER")

	if flags.consumerKey == "" || flags.consumerSecret == "" {
		log.Fatal("Pls enter a valid consumer key and consumer secret")
	}
	config := &clientcredentials.Config{
		ClientID:     flags.consumerKey,
		ClientSecret: flags.consumerSecret,
		TokenURL:     "https://api.twitter.com/oauth2/token",
	}
	httpClient := config.Client(oauth2.NoContext)
	
	
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter the twitter handle :")
	twitter_handle, _ :=reader.ReadString('\n')
	

	client := twitter.NewClient(httpClient)


	userShowParams := &twitter.UserShowParams{ScreenName: twitter_handle}
	user,_,_ := client.Users.Show(userShowParams)
	//fmt.Printf("Basic info:\n%+v\n", user)
	user_s := fmt.Sprintf("%#v",user)
	


	userTimelineParams := &twitter.UserTimelineParams{ScreenName: twitter_handle, Count: 1}
	first_post, _, _ := client.Timelines.UserTimeline(userTimelineParams)
	//fmt.Printf("Latest Post:\n%+v\n",first_post)
	first_post_s := fmt.Sprintf("%#v",first_post)

	txt,_ := os.Create(twitter_handle+".txt")
	size,_ := txt.WriteString(user_s)
	size2,_ := txt.WriteString(first_post_s)
	total_size := size+size2
	t := strconv.Itoa(total_size)
	fmt.Printf(t+"bytes printed")

	

	
}
